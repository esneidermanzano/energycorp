import React from "react";
import CreateClientForm from "views/operator/CreateClientForm.jsx";
import axios from "axios";

import counterpart from "counterpart";
import * as Tr from "react-translate-component";
import spanish from "../../langs/spanish.js";
import english from "../../langs/english.js";
import portuguese from "../../langs/portuguese.js";

import { connect } from "react-redux";

// reactstrap components
import {
    Card,
    CardBody,
    Row,
    Col, Button, Alert
} from "reactstrap";

counterpart.registerTranslations('en', english);
counterpart.registerTranslations('es', spanish);
counterpart.registerTranslations('po', portuguese);

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
                alert(counterpart.translate('createClient.exito'));
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
                        <Tr content="createClient.client" component="i" />
                    </Alert>
                )
            })
        }else{
            news = <center><h6><Tr content="createClient.noUsers" component="i" /></h6></center>;
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
                            <Button color="warning" onClick={this.sendNews}>
                                <Tr content="createClient.create"/>
                            </Button>
                        </center>

                    </Col>
                </Row>
            </div>
        )
    }
};

const mapStateToProps = state => {
    counterpart.setLocale(state.language);
    return { lng: state.language }
}

const mapDispatchToProps = dispatch => ({});

export default connect(mapStateToProps, mapDispatchToProps)(CreateClient);