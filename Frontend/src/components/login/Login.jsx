import React from "react";

import logo from "logo.png";

import auth from "components/auth/auth.js";
import ReCAPTCHA from "react-google-recaptcha";

import { Link } from "react-router-dom";

import {
    Card,
    CardHeader,
    CardBody,
    CardFooter,
    CardTitle,
    Col, Form, FormGroup, Label, Input, Button, Alert
} from "reactstrap";

class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            disabledLoginBtn: true,
            username: '',
            password: '',
            doAnime: false,
            errorLogin: false
        };
    }

    onChange = params => {
        this.setState({
            disabledLoginBtn: false
        });
    };

    handleInput = e => {
        this.setState({
            [e.target.name]: e.target.value
        });
    };

    signin = e => {
        e.preventDefault();
        const delay = 800;
        var data = {username: this.state.username, password: this.state.password};
        if (this.state.username === '100') {

            auth.login(rou => {
                this.setState({ doAnime: true });
                window.setTimeout(() => {
                    this.props.history.push("/" + rou)
                }, delay);

            }, "admin");
        } else if (this.state.username === '200') {

            auth.login(rou => {
                this.setState({ doAnime: true });
                window.setTimeout(() => {
                    this.props.history.push("/" + rou)
                }, delay);

            }, "operator");

        } else if (this.state.username === '300') {

            auth.login(rou => {
                this.setState({ doAnime: true });
                window.setTimeout(() => {
                    this.props.history.push("/" + rou)
                }, delay);

            }, "manager");

        } else {
            document.getElementById("loginForm").reset();
            this.setState({ errorLogin: true });
            window.setTimeout(() => {
                this.setState({ errorLogin: false });
            }, 1500);
        }
    }

    render() {

        const alert = (this.state.errorLogin) ? <Alert className="animated rubberBand" color="danger">
            <center>
                <h6>Verifica la entrada</h6>
            </center>
        </Alert> : true;

        return (
            <div>
                <Col md="4" id="login">
                    {alert}
                    <Card id="cardLogin" className={this.state.doAnime ? "animated zoomOutUp" : ""}>
                        <CardHeader>
                            <center>
                                <img src={logo} width="110px" height="110px" alt="description"></img>
                                <CardTitle tag="h5">Login</CardTitle>
                            </center>
                        </CardHeader>
                        <CardBody>
                            <Form onSubmit={this.signin} id="loginForm">
                                <FormGroup>
                                    <Label for="exampleEmail">ID</Label>
                                    <Input onChange={this.handleInput} type="number" name="username" id="exampleEmail" placeholder="Login" requiered />
                                </FormGroup>
                                <FormGroup>
                                    <Label for="examplePassword">Password</Label>
                                    <Input onChange={this.handleInput} type="password" name="password" id="examplePassword" placeholder="Password" required />
                                </FormGroup>

                                <center>
                                    <ReCAPTCHA
                                        sitekey="6LfP99wUAAAAAPHZbEWQ8x6fXjgBkasCd4ztoqL8"
                                        onChange={this.onChange}
                                    />
                                </center>

                                <center>
                                    <Button color="success" type="submit" disabled={this.state.disabledLoginBtn}>SIGN IN</Button>
                                    <br />
                                    <Link to="/">Home</Link>
                                </center>
                            </Form>
                        </CardBody>
                        <CardFooter>
                        </CardFooter>
                    </Card>
                </Col>
            </div>
        )
    }
}

export default Login;