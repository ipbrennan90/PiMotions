import React, {Component} from "react"
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
  justifyContents: "center",
}

export default class App extends Component {
  constructor(props) {
    super(props)
    this.handleClick = this.handleClick.bind(this)
    this.state = {
      image: "",
    }
  }

  handleClick() {
    axios.get("/take").then(resp => {
      this.setState({image: resp.data.data})
    })
  }

  render() {
    console.log(this.state)
    return (
      <div style={containerStyle}>
        <p>This is a picture hear it roar</p>
        <img style={imgStyle} src={this.state.image} />
        <button style={buttonStyle} onClick={this.handleClick}>
          BUTTON
        </button>
      </div>
    )
  }
}
