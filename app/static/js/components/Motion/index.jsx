import React, { Component } from 'react';

class Motion extends Component {
    render() {
        return (
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
        )
    }
}
