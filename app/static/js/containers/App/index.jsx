import React, { Component } from 'react'
import io from 'socket.io-client'
import { PiConditional, Camera } from '../../components'
import { getMedia, snapshot } from '../../util'
import { Pi } from '../../services'
import './style.css'

import rpi from '../../../assets/raspberrypi.png'
import resin from '../../../assets/resin.png'
import sxsw from '../../../assets/sxsw.png'

const socket = io(process.env.RASPI_URL)

export default class App extends Component {
  constructor(props) {
    super(props)

    this.handleClick = this.handleClick.bind(this)
    this.chooseCam = this.chooseCam.bind(this)
    this.turnOnMotion = this.turnOnMotion.bind(this)
    this.addPic = this.addPic.bind(this)
    this.camera = null

    this.state = {
      image: sxsw,
      webCam: false,
      takeOnPi: true,
      pics: [],
    }
    this.turnOnSocket()
  }

  chooseCam(e) {
    let { value } = e.target

    if (value === 'pi') {
      this.setState({ takeOnPi: true, webcam: false })
    } else {
      getMedia(navigator, () => {
        this.setState({ webCam: true, takeOnPi: false })
      })
    }
  }

  turnOnSocket() {
    socket.on('connect', () => console.log('connected'))
    socket.on('motion response', data => console.log(data))
    socket.on('detector running', data => this.addPic(data))
    socket.on('disconnect', () => console.log('disconnected :('))
  }

  handleClick() {
    if (this.state.takeOnPi) {
      Pi.takePicture().then(picture => {
        this.setState({ image: picture.data.src })
      })
    } else {
      snapshot(this.camera, this)
    }
  }

  turnOnMotion() {
    if (this.state.motionDetector === 'on') {
      socket.emit('motion', 'off')
      this.setState({ motionDetector: 'off' })
    } else {
      socket.emit('motion', 'on')
      this.setState({ motionDetector: 'on' })
    }
  }
  addPic(data) {
    const { pic } = data
    this.setState(prevState => {
      pics: prevState.pics.push(pic)
    })
  }

  renderPicStream(pics) {
    return pics.map(pic => {
      return <img style={imgStyle} src={pic} />
    })
  }

  render() {
    const { isPi, takeOnPi, image } = this.state

    return (
      <div className="container">
        <header className="header">
          <h1>Take My Picture</h1>
        </header>
        <PiConditional chooseCam={this.chooseCam} selected={takeOnPi} />
        <Camera
          innerRef={camera => (this.camera = camera)}
          takeOnPi={takeOnPi}
          image={image}
        />
        <button className="button trigger" onClick={this.handleClick}>
          Take Picture
        </button>
        <button className="button" onClick={this.turnOnMotion}>
          TURN MOTION DETECTOR{' '}
          {this.state.motionDetector === 'on' ? 'OFF' : 'ON'}
        </button>
        {pics.length > 0 && this.renderPicStream(pics)}

        <hr />
        <footer className="footer">
          <a href="https://raspberrypi.org/" target="_blank">
            <img src={rpi} />
          </a>
          <a href="https://resin.io" target="_blank">
            <img src={resin} />
          </a>
        </footer>
      </div>
    )
  }
}
