import React from "react";
import CreateUserForm from "views/admin/CreateUserForm.jsx";

import counterpart from "counterpart";
import * as Tr from "react-translate-component";
import spanish from "../../langs/spanish.js";
import english from "../../langs/english.js";
import portuguese from "../../langs/portuguese.js";

// reactstrap components
import {
    Card,
    CardBody,
    Row,
    Col, Button, Alert
} from "reactstrap";
import Axios from "axios";

import { connect } from "react-redux";

counterpart.registerTranslations('en', english);
counterpart.registerTranslations('es', spanish);
counterpart.registerTranslations('po', portuguese);

class CreateUser extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            list: []
        }
    }

    createEle = item => {
        // Hay que cambiarlo a numero para que se envie con esa informacion
        console.log(item.user_type)
        if (item.user_type === 'Gerente' || item.user_type === 'Manager') {
            item.user_type = 2;
        } else if (item.user_type === 'Operador' || item.user_type === "Operator") {
            item.user_type = 3;
        }

        // console.log(item)

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

    parseToSend = user => {
        let parsed = {
            user_type: user.user_type,
            user: {
                id_user: user.id_user,
                name: user.name,
                email: user.email,
                password: user.password,
                phone: user.phone,
                address: user.address,
                neighborhood: user.neighborhood,
                // stratus: user.stratus,
                is_active: user.is_active,
                is_staff: user.is_staff,
                is_superuser: user.is_superuser
            }
        }

        return parsed;
    }

    sendNews = () => {
        // AXIOS
        var data = [];

        for (let i = 0; i < this.state.list.length; i++) {
            let user = this.state.list[i];
            data.push(this.parseToSend(user));
        }

        // console.log(data)

        Axios.post('https://energycorp.herokuapp.com/api/user/worker/create/bulk/', data)
            .then(res => {
                let given = res.data;
                if (given.code === 200) {
                    alert(counterpart.translate('createUser.exito'));
                } else {
                    alert(counterpart.translate('createUser.noExito'));
                }
            })
            .catch(err => {
                console.log(err);
            })

        console.log(data);
        this.setState({ list: [] });
    }

    render() {
        var news = this.state.list;
        if (news.length !== 0) {
            news = this.state.list.map((n, key) => {
                return (
                    <Alert color="success" key={key} toggle={() => this.onDismiss(key)}>
                        #{key + 1} <b>{n.name}</b> - {n.id_user}
                        <br></br>
                        <i>{(n.user_type === 3) ? counterpart.translate('createUser.operator') :
                            counterpart.translate('createUser.manager')}</i>
                    </Alert>
                )
            })
        } else {
            news = <center><h6><Tr content="createClient.noUsers" component="i" /></h6></center>;
        }

        return (
            <div className="content">
                <Row>
                    <Col md="6" >
                        <Card>
                            <CardBody>
                                <CreateUserForm submitAction={this.createEle} editMode={false} />
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
                            <Button color="success" onClick={this.sendNews}>
                                <Tr content="createClient.create" />
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

export default connect(mapStateToProps, mapDispatchToProps)(CreateUser);