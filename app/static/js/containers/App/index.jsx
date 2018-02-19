import React, {Component} from 'react'
import axios from 'axios'
import './style.css'
import {getMedia, snapshot} from '../../util'
import {Pi} from '../../services'
import {PiConditional, Camera} from '../../components'

export default class App extends Component {
  constructor(props) {
    super(props)
    this.handleClick = this.handleClick.bind(this)
    this.chooseCam = this.chooseCam.bind(this)
    this.camera = null
    this.state = {
      image: '',
      webCam: false,
      takeOnPi: true,
    }
  }

  chooseCam(cam) {
    if (cam === 'pi') {
      this.setState({takeOnPi: true})
    } else {
      getMedia(navigator, () => {
        this.setState({webCam: true, takeOnPi: false})
      })
    }
  }

  handleClick() {
    if (this.state.takeOnPi) {
      Pi.takePicture().then(picture => {
        this.setState({image: picture.data.src})
      })
    } else {
      snapshot(this.camera, this)
    }
  }

  render() {
    const {takeOnPi} = this.state

    return (
      <div className="container">
        <PiConditional chooseCam={this.chooseCam} />
        <Camera innerRef={camera => (this.camera = camera)} />
        <button className="button" onClick={this.handleClick}>
          TAKE PICTURE
        </button>
      </div>
    )
  }
}
