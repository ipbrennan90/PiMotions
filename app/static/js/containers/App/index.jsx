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
      motionDetection: false,
      sensitivity: null,
      threshold: null,
      detectionData: {
        motion: false,
        pixChanged: 0,
      },
    }
  }

  turnOnSocket() {
    socket.on('connect', () => {
      this.setState({ motionDetection: true })
    })
    socket.on('motion response', data => console.log(data))
    socket.on('motion-data', data => {
      console.log(data)
      this.setState({ detectionData: data })
    })
    socket.on('sensitivity', data => {
      this.setState({ sensitivity: data.sensitivity })
    })
    socket.on('threshold', data => {
      this.setState({ threshold: data.threshold })
    })
    socket.on('motion-detector-exit', data => console.log(data))
    socket.on('disconnect', () => {
      this.setState({ motionDetection: false })
    })
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

  handleSensitivityChange(e) {
    console.log(e.target.value)
    socket.emit('set-sensitivity', e.target.value)
  }

  handleThresholdChange(e) {
    console.log(e.target.value)
    socket.emit('set-threshold', e.target.value)
  }

  turnOnMotion() {
    if (this.state.motionDetector === 'on') {
      socket.emit('stop-cam')
      this.setState({
        motionDetector: 'off',
        detectionData: {
          motion: false,
          pixChanged: 0,
        },
      })
    } else {
      socket.emit('motion-start')
      this.setState({ motionDetector: 'on' })
    }
  }

  addPic(data) {
    const { pic } = data
    this.setState(prevState => {
      pics: prevState.pics.push(pic)
    })
  }

  render() {
    const {
      isPi,
      takeOnPi,
      image,
      motionDetection,
      sensitivity,
      threshold,
      detectionData,
    } = this.state

    const motionBackground = detectionData.motion ? 'green' : 'red'
    const motionWidth = detectionData.pixChanged / 500 * 100
    return (
      <div className="container">
        <header className="header">
          <h1>PiMotions</h1>
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

        {this.state.motionDetection && (
          <div style={{ width: '100%', height: '300px' }}>
            <button className="button" onClick={this.turnOnMotion}>
              TURN MOTION DETECTOR{' '}
              {this.state.motionDetector === 'on' ? 'OFF' : 'ON'}
            </button>
            <div style={{ width: '100%', height: '50px' }}>
              <div
                style={{
                  width: `${motionWidth}%`,
                  height: '100%',
                  backgroundColor: `${motionBackground}`,
                }}
              />
            </div>
            <label
              style={{
                width: '100%',
                height: '20px',
                marginTop: '20px',
                marginBottom: '20px',
                display: 'block',
              }}
              htmlFor="sensitivity"
            >
              sensitivity: {this.state.sensitivity}
            </label>
            <input
              type="range"
              onMouseUp={this.handleSensitivityChange}
              id="sensitivity"
              min="0"
              defaultValue="20"
              max="500"
              step="1"
              style={{ width: '100%' }}
            />
            <label
              style={{
                width: '100%',
                height: '20px',
                marginTop: '20px',
                marginBottom: '20px',
                display: 'block',
              }}
              htmlFor="threshold"
            >
              threshold: {this.state.threshold}
            </label>
            <input
              type="range"
              onMouseUp={this.handleThresholdChange}
              id="threshold"
              min="0"
              defaultValue="10"
              max="500"
              step="1"
              style={{ width: '100%' }}
            />
          </div>
        )}

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
