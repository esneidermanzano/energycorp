import React from "react";
import CreateClientForm from "views/operator/CreateClientForm.jsx";
// import axios from 'axios';

import counterpart from "counterpart";
import * as Tr from "react-translate-component";
import spanish from "../../langs/spanish.js";
import english from "../../langs/english.js";
import portuguese from "../../langs/portuguese.js";

import { connect } from "react-redux";

import {
    Card,
    CardBody,
    Row,
    Col, FormGroup, Input, Button, Table,
    Modal, ModalHeader, ModalBody
} from "reactstrap";

counterpart.registerTranslations('en', english);
counterpart.registerTranslations('es', spanish);
counterpart.registerTranslations('po', portuguese);

class GetClients extends React.Component {
    constructor(props) {
        super(props);
        this.state = { //PHONE IS NUMBER
            persons: [],
            search: '',
            modal: false,
            selected: 'All',
            user: {},
        }
    }

    handleInput = e => {
        this.setState({
            [e.target.name]: e.target.value
        });
    }

    openToggle = obj => {
        this.setState({
            user: obj,
            modal: true
        });
    }

    closeToggle = () => {
        this.setState({
            modal: false
        });
    }

    editUser = state => {
        // alert('Axios');
        // axios.post("https://energycorp.herokuapp.com/api/user/client/" + state.id + "/update/", state)
        //     .then(res => {
        //         alert("AXION REALIZADA CON EXITO");
        //     })
        //     .catch(err => {
        //         console.log(err);
        //     })
        this.closeToggle();
    }

    async componentDidMount() {
        const res = await fetch('https://energycorp.herokuapp.com/api/user/client/');

        const data = await res.json();

        this.setState({ persons: data });
    }

    render() {

        var filteredPeople = [];

        filteredPeople = this.state.persons.filter(p => (
            p.user.email.toLowerCase().indexOf(this.state.search.toLowerCase()) !== -1
        ));

        const people = filteredPeople.map((p, k) => (
            <tr key={k}>
                <th scope="row">#{k + 1}</th>
                <th>{p.user.id_user}</th>
                <th>{p.user.name}</th>
                <th>{p.user.phone}</th>
                <th>{p.user.email}</th>
                <th>
                    <Button color="warning" onClick={() => this.openToggle(p)}>
                        <i className="nc-icon nc-zoom-split" />
                    </Button>
                </th>
            </tr>
        ));

        const placeholderSearch = counterpart.translate('getClients.search');

        return (
            <div className="content">
                <Row>
                    <Col sm="12">
                        <br></br>
                        <Card >
                            <CardBody>
                                <Col>
                                    <Row>
                                        <FormGroup>
                                            <Input onChange={this.handleInput} name="search" placeholder={placeholderSearch}></Input>
                                        </FormGroup>
                                    </Row>
                                    <br></br>
                                    <Table responsive>
                                        <thead>
                                            <tr>
                                                <th>#</th>
                                                <th>ID</th>
                                                <th>
                                                    <Tr content="clientForm.name"/>
                                                </th>
                                                <th>
                                                    <Tr content="clientForm.phone"/>
                                                </th>
                                                <th>Email</th>
                                                <th>
                                                    <Tr content="getClients.review"/>
                                                </th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {people}
                                        </tbody>
                                    </Table>
                                </Col>
                            </CardBody>
                        </Card>
                    </Col>

                    <div>
                        <Modal md="7" isOpen={this.state.modal} toggle={this.closeToggle} className="danger">
                            <ModalHeader toggle={this.closeToggle}>
                                <Tr content="getClients.edit"/>
                            </ModalHeader>
                            <ModalBody>
                                <CreateClientForm submitAction={this.editUser} user={this.state.user} editMode={true} />
                            </ModalBody>
                        </Modal>
                    </div>

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

export default connect(mapStateToProps, mapDispatchToProps)(GetClients);