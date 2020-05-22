import React from "react";
// react plugin used to create charts
import { Bar, Pie } from "react-chartjs-2";

// reactstrap components
import {
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  CardTitle,
  Row,
  Col,
  Button
} from "reactstrap";

class CreateReports extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        rInit: true,
        r1: false,
        r2: false,
        pieChartData: {},
        barChartDataHighest: {},
        barChartDataLowest: {}
    }
  }

  async componentDidMount() {

    // PieChartData
    const res = await fetch('https://energycorp.herokuapp.com/api/reports/moraandsuspended/');

    const data = await res.json();

    let newPieChartData = {
      datasets: [{
        data: [data.numclientsmora, data.numclientsuspended],
        backgroundColor: ['red', 'yellow']
      }],
      labels: [
        'Slow Payers',
        'Suspended Clients'
      ]
    };

    this.setState({pieChartData: newPieChartData});

    // BarChartDataHighest
    const resBar = await fetch('https://energycorp.herokuapp.com/api/reports/topfive/');

    const dataBar = await resBar.json();
    console.log(dataBar)

    let newBarChartDataHighest = {
      labels: [dataBar.topfiveplus[0].codeCounter, dataBar.topfiveplus[1].codeCounter, dataBar.topfiveplus[2].codeCounter, dataBar.topfiveplus[4].codeCounter, dataBar.topfiveplus[4].codeCounter],
      datasets: [{
        label: 'Power Consumption',
        data: [
          dataBar.topfiveplus[0].value,
          dataBar.topfiveplus[1].value,
          dataBar.topfiveplus[2].value,
          dataBar.topfiveplus[3].value,
          dataBar.topfiveplus[4].value
        ],
        backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(255,206, 86, 0.6)',
          'rgba(75, 192, 192, 0.6)',
          'rgba(153, 102, 255, 0.6)',
        ]
      }
      ]
    };
    // BarChartDataLowest
    let newBarChartDataLowest = {
      labels: [dataBar.topfiveplus[4].codeCounter, dataBar.topfiveplus[3].codeCounter, dataBar.topfiveplus[2].codeCounter, dataBar.topfiveplus[1].codeCounter, dataBar.topfiveplus[0].codeCounter],
      datasets: [{
        label: 'Power Consumption',
        data: [
          dataBar.topfiveminus[4].value,
          dataBar.topfiveminus[3].value,
          dataBar.topfiveminus[2].value,
          dataBar.topfiveminus[1].value,
          dataBar.topfiveminus[0].value
        ],
        backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(255,206, 86, 0.6)',
          'rgba(75, 192, 192, 0.6)',
          'rgba(153, 102, 255, 0.6)',
        ]
      }
      ]
    };
    console.log('HOLA', newBarChartDataHighest);
    this.setState({barChartDataHighest: newBarChartDataHighest});
    this.setState({barChartDataLowest: newBarChartDataLowest});

  }

  renderR1 = () => {
    this.setState({
        rInit: false,
        r1: true,
        r2: false,
        r3: false
    });
  }

  renderR2 = () => {
    this.setState({
        rInit: false,
        r1: false,
        r2: true,
        r3: false
    });
  }

  renderR3 = () => {
    this.setState({
        rInit: false,
        r1: false,
        r2: false,
        r3: true
    });
  }

  render() {
    return (
        <div className="content">
          <Row>
            <Col md="4">
              <Card>
                <CardHeader>
                  <CardTitle tag="h5">Choose a report</CardTitle>
                  <p className="card-category">From the following options</p>
                </CardHeader>
                <CardBody>
                  <Button color="primary" onClick={this.renderR1}>Clients' financial status (number of each)
                  </Button>
                  <br/>
                  <Button color="primary" onClick={this.renderR2}>Highest Consuming Transformers
                  </Button>
                  <br/>
                  <Button color="primary" onClick={this.renderR3}>Lowest Consuming Transformers
                  </Button>
                </CardBody>
                <CardFooter>
                </CardFooter>
              </Card>
            </Col>
            <Col md="8">
              <Card className="card-chart">
                <CardHeader>
                  <CardTitle tag="h5">Currently Chosen Report</CardTitle>
                  <p className="card-category">-----</p>
                </CardHeader>
                <CardBody>
                  {
                    this.state.rInit ? (
                      <div>
                       <p>
                         Choose a report from the options on your left side
                       </p>
                      </div>
                    ) : true
                  }
                  {
                    this.state.r1 ? (
                      <div>
                        <p>
                         Number of Slow Payers and Suspended Users
                       </p>
                       <Pie
                        data = {{
                          labels: this.state.pieChartData.labels,
                          datasets: this.state.pieChartData.datasets
                        }}
                       />
                      </div>
                    ) : true
                  }
                  {
                    this.state.r2 ? (
                      <div>
                        <p>
                        Highest consuming transformers
                       </p>
                       <Bar
                        data = {this.state.barChartDataHighest}
                        options = {{
                          maintainAspectRatio: true
                        }}
                       />
                      </div>
                    ) : true
                  }
                  {
                    this.state.r3 ? (
                      <div>
                        <p>
                        Lowest consuming transformers
                       </p>
                       <Bar
                        data = {this.state.barChartDataLowest}
                        options = {{
                          maintainAspectRatio: true
                        }}
                       />
                      </div>
                    ) : true
                  }
                  
                </CardBody>
                <CardFooter>
                  <hr />
                  <div className="card-stats">
                    <i className="fa fa-check" /> Data information certified
                  </div>
                </CardFooter>
              </Card>
            </Col>
          </Row>
        </div>
    );
  }
}

export default CreateReports;
