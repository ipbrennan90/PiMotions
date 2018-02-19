import React, {Component} from "react"
import ReactCamera from "simple-react-camera"
import axios from "axios"
import "./App.css"
import {getDevices} from "./util"

export default class App extends Component {
  constructor(props) {
    super(props)
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
      getDevices(navigator, () => {
        this.setState({webCam: true, takeOnPi: false})
      })
    }
  }

  handleClick() {
    console.log(process.env.raspiurl)
    if (this.state.takeOnPi) {
      axios.get(`${process.env.RASPI_URL}/take`).then(resp => {
        this.setState({image: resp.data.data})
      })
    } else {
      this.camera
        .snapshot()
        .then(data => {
          /* data: string (base-64-jqeg)
               Process your data here*/
          this.setState({image: data})
        })
        .catch(console.error)
    }
  }

  render() {
    const {takeOnPi} = this.state

    return (
      <div className="container">
        <div className="pi_conditional">
          <p>Use camera on pi?</p>
          <button
            onClick={() => {
              this.chooseCam("pi")
            }}
          >
            YES
          </button>
          <button
            onClick={() => {
              this.chooseCam("web")
            }}
          >
            NO
          </button>
        </div>
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
