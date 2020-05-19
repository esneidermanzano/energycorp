import React from "react";
import CreateUserForm from "views/admin/CreateUserForm.jsx";

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

class GetUser extends React.Component {
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

    editUser = () => {
        this.closeToggle();
    }

    parseToShow = user => {
        let parsed = {
            user_type: '',
            id_user: user.user.id_user,
            name: user.user.name,
            email: user.user.email,
            address: user.user.address,
            neighborhood: user.user.neighborhood,
            phone: user.user.phone,
            stratus: user.user.stratus,
            is_active: user.user.is_active,
        }

        if (user.user_type === 2) {
            parsed.user_type = 'gerente';
        } else if (user.user_type === 3) {
            parsed.user_type = 'operador';
        }
        return parsed;

    }

    render() {

        const trans = (tipo) => {
            if (tipo === 'operador') {
                return counterpart.translate('createUser.operator');
            } else {
                return counterpart.translate('createUser.manager');
            }
        }

        var filteredPeople = [];

        if (this.state.selected !== counterpart.translate('getUser.all')) {
            //Filtrar por ambas formas al tiempo
            filteredPeople = this.state.persons.filter(p => (
                trans(p.user_type).toLowerCase() === this.state.selected.toLowerCase() &&
                p.email.toLowerCase().indexOf(this.state.search.toLowerCase()) !== -1
            ));
        } else { //Filtrar solo por busqueda
            filteredPeople = this.state.persons.filter(p => (
                p.email.toLowerCase().indexOf(this.state.search.toLowerCase()) !== -1
            ));
        }

        const people = filteredPeople.map((p, k) => (
            <tr key={k}>
                <th scope="row">#{k + 1}</th>
                <th>{p.name}</th>
                <th>{p.id_user}</th>
                <th>{p.email}</th>
                <th>{trans(p.user_type)}</th>
                <th>
                    <Button color="success" onClick={() => this.openToggle(p)}>
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
                                        <Col>
                                            <select onChange={this.handleInput} className="form-control" name="selected">
                                                <Tr content="getUser.all" component="option" />
                                                <Tr content="createUser.operator" component="option" />
                                                <Tr content="createUser.manager" component="option" />
                                            </select>
                                        </Col>
                                        <Col>
                                            <FormGroup>
                                                <Input onChange={this.handleInput} name="search" placeholder={placeholderSearch}></Input>
                                            </FormGroup>
                                        </Col>
                                    </Row>
                                    <br></br>
                                    <Table responsive>
                                        <thead>
                                            <tr>
                                                <th>#</th>
                                                <th><Tr content="clientForm.name" /></th>
                                                <th>ID</th>
                                                <th>Email</th>
                                                <th><Tr content="clientForm.type" /></th>
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
                                <Tr content="getClients.edit" />
                            </ModalHeader>
                            <ModalBody>
                                <CreateUserForm submitAction={this.editUser} user={this.state.user} editMode={true} />
                            </ModalBody>
                        </Modal>
                    </div>

                </Row>
            </div>
        )
    }

    async componentDidMount() {
        const res = await fetch('https://energycorp.herokuapp.com/api/user/worker/');
        const data = await res.json();
        // console.log(data)
        var parsedData = [];
        for (let i = 0; i < data.length; i++) {
            if (data[i].user_type !== 1) {
                parsedData.push(this.parseToShow(data[i]));
            }
        }

        this.setState({ persons: parsedData });
    }

};

const mapStateToProps = state => {
    counterpart.setLocale(state.language);
    return { lng: state.language }
}

const mapDispatchToProps = dispatch => ({});

export default connect(mapStateToProps, mapDispatchToProps)(GetUser);

