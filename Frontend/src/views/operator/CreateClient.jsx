import React from "react";
import CreateClientForm from "views/operator/CreateClientForm.jsx";
import axios from "axios";

// reactstrap components
import {
    Card,
    CardBody,
    Row,
    Col, Button, Alert
} from "reactstrap";

class CreateClient extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            list: []
        }
    }

    createEle = item => {
        this.setState({
            list: [...this.state.list, item]
        })
    }

    onDismiss = key => {
        var newList = this.state.list.slice();
        newList.splice(key, 1);
        this.setState({
            list: newList
        })
    }

    sendNews = () => {
        // AXIOS
        // alert("Axios");
        console.log(this.state.list);
        axios.post("https://energycorp.herokuapp.com/api/user/client/create/bulk/", this.state.list)
            .then(res => {
                alert("AXION REALIZADA CON EXITO");
            })
            .catch(err => {
                console.log(err);
            })
        this.setState({ list: [] });
    }

    render() {

        var news = this.state.list;
        if (news.length !== 0) {
            news = this.state.list.map((n, key) => {
                return (
                    <Alert color="warning" key={key} toggle={() => this.onDismiss(key)}>
                        #{key + 1} <b>{n.user.name}</b> - {n.user.id_user}
                        <br></br>
                        <i>Cliente</i>
                    </Alert>
                )
            })
        }else{
            news = <center><h6><i>No users yet</i></h6></center>;
        }

        return (
            <div className="content">
                <Row>
                    <Col md="6" >
                        <Card>
                            <CardBody>
                                <CreateClientForm submitAction={this.createEle} editMode={false}/>
                            </CardBody>
                        </Card>
                    </Col>
                    <Col md="6">
                        <Card>
                            <CardBody>
                                {news}
                            </CardBody>
                        </Card>
                        <center>
                            <Button color="warning" onClick={this.sendNews}>CREATE</Button>
                        </center>

                    </Col>
                </Row>
            </div>
        )
    }
};

export default CreateClient;