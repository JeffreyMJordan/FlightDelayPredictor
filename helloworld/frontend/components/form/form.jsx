import React from 'react';

export default class Form extends React.Component {
  // constructor(props) {
  //   super(props);
  //
  // }

  render() {
    return (
      <div className="form-cont">
        <input type="text" placeholder="Origin Airport"></input>
        <input type="text" placeholder="Destination Airport"></input>
        <input type="text" placeholder="Airline"></input>
        <input type="date" placeholder="Date"></input>
        <input type="time" placeholder="Time"></input>
        <button type="submit">Analyze Flight</button>
        {/* Hey Eden sorry to mess w your front end, just tryna test the estimator we have rn below */}
        <input type="text" />
      </div>
    );
  }
}