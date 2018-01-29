import React, {Component} from "react"
import axios from "axios"

const imgStyle = {
  height: "200px",
  width: "200px",
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
      console.log("i am the egg man")
      this.setState({image: resp.data.data})
    })
  }

  render() {
    console.log(this.state)
    return (
      <div>
        <p>This is a picture hear it roar</p>
        <img style={imgStyle} src={this.state.image} />
        <button onClick={this.handleClick}>BUTTON</button>
      </div>
    )
  }
}
