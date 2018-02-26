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
  }

  turnOnSocket() {
    socket.on('connect', () => console.log('connected'))
    socket.on('motion response', data => console.log(data))
    socket.on('detector running', data => {
      console.log(data)
      let { pics } = this.state
      pics.push({
        img: data.pic,
        img_diff: data.diff_img,
        entropy: data.entropy,
      })

      this.setState({ pics })
    })
    socket.on('disconnect', () => socket.emit('disconnect', 'disconnected'))
  }

  componentDidMount() {
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
      if (!pic.entropy) return
      return (
        <span>
          <img src={pic.img_diff} />
          <p>TOTAL ENTROPY: {pic.entropy.total_entropy.entropy}</p>
          <p>
            R ENTROPY: {pic.entropy.r_entropy.entropy} LENGTH:{' '}
            {pic.entropy.r_entropy.length}
          </p>
          <p>
            G ENTROPY: {pic.entropy.g_entropy.entropy} LENGTH:{' '}
            {pic.entropy.g_entropy.length}
          </p>
          <p>
            B ENTROPY: {pic.entropy.b_entropy.entropy} LENGTH:{' '}
            {pic.entropy.b_entropy.length}
          </p>
        </span>
      )
    })
  }

  render() {
    const { isPi, takeOnPi, image, pics } = this.state

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
        {this.renderPicStream(pics)}

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
