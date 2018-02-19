import React, {Component} from "react"
import ReactCamera from "simple-react-camera"
import axios from "axios"
import "./App.css"
import {getMedia, snapshot} from "./util"
import {PiConditional} from "./components"

export default class App extends Component {
  constructor(props) {
    super(props)
    debugger
    this.handleClick = this.handleClick.bind(this)
    this.chooseCam = this.chooseCam.bind(this)
    this.camera = null
    this.state = {
      image: "",
      webCam: false,
      takeOnPi: true,
    }
  }

  chooseCam(cam) {
    if (cam === "pi") {
      this.setState({takeOnPi: true})
    } else {
      getMedia(navigator, () => {
        this.setState({webCam: true, takeOnPi: false})
      })
    }
  }

  handleClick() {
    if (this.state.takeOnPi) {
      axios.get(`${process.env.RASPI_URL}/take`).then(resp => {
        this.setState({image: resp.data.data})
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
        <div className="image_container">
          {!takeOnPi && (
            <ReactCamera
              className={"yourCssClassHere"}
              ref={camera => (this.camera = camera)}
              width={800}
              height={500}
            />
          )}
          <img className="image" src={this.state.image} />
        </div>
        <button className="button" onClick={this.handleClick}>
          TAKE PICTURE
        </button>
      </div>
    )
  }
}
