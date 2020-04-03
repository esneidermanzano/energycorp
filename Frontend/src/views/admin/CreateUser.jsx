import React from "react";
import CreateUserForm from "views/admin/CreateUserForm.jsx";

// reactstrap components
import {
    Card,
    CardBody,
    Row,
    Col, Button, Alert
} from "reactstrap";
import Axios from "axios";

class CreateUser extends React.Component {
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
                stratus: user.stratus,
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

        Axios.post('https://energycorp.herokuapp.com/api/user/worker/create/bulk/', data)
        .then(res => {
            let given = res.data;
            if(given.code === 200){
                alert('Registro exitoso.');
            }else{
                alert('Algo salió mal.');
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
                        <i>{n.user_type}</i>
                    </Alert>
                )
            })
        } else {
            news = <center><h6><i>No users yet</i></h6></center>;
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
                            <Button color="success" onClick={this.sendNews}>CREATE</Button>
                        </center>

                    </Col>
                </Row>
            </div>
        )
    }
};

export default CreateUser;