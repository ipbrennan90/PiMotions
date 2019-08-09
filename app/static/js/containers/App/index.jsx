import React, { Component } from "react";
import io from "socket.io-client";
import { PiConditional, Camera, Motion } from "../../components";
import { getMedia } from "../../util";
import { Pi } from "../../services";
import "./style.css";

import rpi from "../../../assets/raspberrypi.png";
import resin from "../../../assets/resin.png";
import sxsw from "../../../assets/sxsw.png";

const socket = io(process.env.RASPI_URL, {
  transports: ["websocket", "polling", "flashsocket"]
});

export default class App extends Component {
  constructor(props) {
    super(props);

    this.handleClick = this.handleClick.bind(this);
    this.chooseCam = this.chooseCam.bind(this);
    this.turnOnMotion = this.turnOnMotion.bind(this);
    this.addPic = this.addPic.bind(this);
    this.camera = null;

    this.state = {
      image: sxsw,
      webCam: false,
      takeOnPi: true,
      pics: [],
      motionDetection: false,
      motionDetector: "off",
      sensitivity: null,
      threshold: null,
      detectionData: {
        motion: false,
        pixChanged: 0
      }
    };
  }

  turnOnSocket() {
    socket.on("connect", () => {
      this.setState({ motionDetection: true });
    });
    socket.on("motion-data", data => {
      if (this.state.motionDetector === "on") {
        this.setState({ detectionData: data });
      }
    });
    socket.on("sensitivity", data => {
      this.setState({ sensitivity: data.sensitivity });
    });
    socket.on("threshold", data => {
      this.setState({ threshold: data.threshold });
    });
    socket.on("motion-detector-exit", data => console.warn(data));
    socket.on("disconnect", () => {
      this.setState({ motionDetection: false });
    });
  }

  componentDidMount() {
    this.turnOnSocket();
  }

  chooseCam(e) {
    let { value } = e.target;

    if (value === "pi") {
      this.setState({ takeOnPi: true, webcam: false });
    } else {
      getMedia(navigator, () => {
        this.setState({ webCam: true, takeOnPi: false });
      });
    }
  }

  handleClick() {
    if (this.state.takeOnPi) {
      Pi.takePicture().then(picture => {
        this.setState({ image: picture.data.src });
      });
    } else {
      this.camera
        .snapshot()
        .then(data => {
          this.setState({ image: data });
        })
        .catch(console.error);
    }
  }

  handleSensitivityChange(e) {
    socket.emit("set-sensitivity", e.target.value);
  }

  handleThresholdChange(e) {
    socket.emit("set-threshold", e.target.value);
  }

  turnOnMotion() {
    if (this.state.motionDetector === "on") {
      socket.emit("stop-cam");
      this.setState({
        motionDetector: "off",
        detectionData: {
          motion: false,
          pixChanged: 0
        }
      });
    } else {
      socket.emit("motion-start");
      this.setState({ motionDetector: "on" });
    }
  }

  addPic(data) {
    const { pic } = data;
    this.setState(prevState => {
      pics: prevState.pics.push(pic);
    });
  }

  render() {
    const {
      isPi,
      takeOnPi,
      image,
      motionDetection,
      motionDetector,
      sensitivity,
      threshold,
      detectionData
    } = this.state;

    const motionBackground = detectionData.motion ? "green" : "red";
    const motionChange =
      detectionData.pixChanged > 500 ? 500 : detectionData.pixChanged;
    const motionWidth = (motionChange / 500) * 100;
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
        <button className="button trigger icon" onClick={this.handleClick}>
          Take Picture
        </button>

        {this.state.motionDetection && (
          <Motion
            turnOnMotion={this.turnOnMotion}
            motionDetector={motionDetector}
            motionWidth={motionWidth}
            motionBackground={motionBackground}
            sensitivity={sensitivity}
            handleSensitivityChange={this.handleSensitivityChange}
            threshold={threshold}
            handleThresholdChange={this.handleThresholdChange}
          />
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
    );
  }
}
