import React, {Component} from "react"
import ReactCamera from "simple-react-camera"
import axios from "axios"

const imgStyle = {
  height: "200px",
  width: "200px",
}

const buttonStyle = {
  height: "20px",
  width: "200px",
}

const containerStyle = {
  display: "flex",
  flexDirection: "column",
  justifyContent: "center",
  alignItems: "center",
}

const piConditionalStyle = {
  width: "200px",
  height: "80px",
}

const imageStyle = {
  display: "flex",
  flexDirection: "row",
  flexBasis: "auto",
  justifyContent: "space-around",
}

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

  componentDidMount() {
    const app = this
    navigator.getMedia =
      navigator.getUserMedia || // use the proper vendor prefix
      navigator.webkitGetUserMedia ||
      navigator.mozGetUserMedia ||
      navigator.msGetUserMedia

    navigator.getMedia(
      {video: true},
      function() {
        app.setState({webCam: true})
      },
      function() {
        alert("NO WEBCAM")
      },
    )
  }

  chooseCam(cam) {
    if (cam === "pi") {
      this.setState({takeOnPi: true})
    } else {
      this.setState({takeOnPi: false})
    }
  }

  handleClick() {
    if (this.state.takeOnPi) {
      axios.get("/take").then(resp => {
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
      <div style={containerStyle}>
        <div style={piConditionalStyle}>
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
        <div style={imageStyle}>
          {!takeOnPi && (
            <ReactCamera
              classNames={"yourCssClassHere"}
              ref={camera => (this.camera = camera)}
              width={800}
              height={500}
            />
          )}
          <img style={imgStyle} src={this.state.image} />
        </div>
        <button style={buttonStyle} onClick={this.handleClick}>
          TAKE PICTURE
        </button>
      </div>
    )
  }
}
