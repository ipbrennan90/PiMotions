import React, { Component } from 'react'
import { PiConditional, Camera } from '../../components'
import { getMedia, snapshot } from '../../util'
import { Pi } from '../../services'
import './style.css'

import rpi from '../../../assets/raspberrypi.png'
import resin from '../../../assets/resin.png'
import sxsw from '../../../assets/sxsw.png'

export default class App extends Component {
  constructor(props) {
    super(props)

    this.handleClick = this.handleClick.bind(this)
    this.chooseCam = this.chooseCam.bind(this)
    this.camera = null

    this.state = {
      image: sxsw,
      webCam: false,
      takeOnPi: true
    }
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
