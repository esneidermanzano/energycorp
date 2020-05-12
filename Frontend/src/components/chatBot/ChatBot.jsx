import React from "react";

import counterpart from "counterpart";
// import * as Tr from "react-translate-component";
// import spanish from "../../langs/spanish.js";
// import english from "../../langs/english.js";

import {
    Card, Row, CardBody,
    Col, Input, Form, FormGroup, CardFooter,
    ListGroup, ListGroupItem
} from "reactstrap";

import axios from 'axios';

import bot_gif from "./bot_gif.gif";

import { connect } from "react-redux";

// counterpart.registerTranslations('en', english);
// counterpart.registerTranslations('es', spanish);

// counterpart.setLocale('en');

class ChatBot extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            msg: "",
            chats: []
        }
    }

    handleInput = e => {
        this.setState({ [e.target.name]: e.target.value });
    }

    closeChat = () => {
        this.props.close();
    }

    sendMsg = e => {
        e.preventDefault();
        if (this.state.msg !== "") {

            this.setState((prev, props) => {
                return { chats: [...this.state.chats, this.state.msg], msg: "" };
            });

            const config = {
                headers: { Authorization: 'Bearer 9121e7b53d944b4a8088cd12b17df3ac' }
            };

            var obj = {
                "lang": "es",
                "query": this.state.msg,
                "sessionId": "12345",
                "timezone": "America/New_York",
                "headers": {
                    'Content-Type': 'application/json'
                }
            }

            axios.post("https://api.dialogflow.com/v1/query?v=20170712", obj, config)
                .then(res => {
                    this.setState((prev, props) => {
                        return { chats: [...this.state.chats, res.data.result.fulfillment.speech], msg: "" };
                    });
                    var messageBody = document.querySelector('#chat_box');
                    messageBody.scrollTop = messageBody.scrollHeight;
                })
                .catch(err => {
                    console.log(err);
                })



            // setTimeout(() => {
            //     var messageBody = document.querySelector('#chat_box');
            //     messageBody.scrollTop = messageBody.scrollHeight;
            // });

        }
    }

    render() {
        return (
            <div>
                <div className="floatingChat">
                    <Col md="12" id="chat">
                        <center className="animated wobble">
                            <img className="bot_on_chat" onClick={this.closeChat} src={bot_gif} width="95px" height="120px" alt="description" ></img>
                        </center>
                        <Card className="animated wobble">
                            <CardBody style={{ "backgroundColor": " #d4d4d4 " }}>
                                <div className="msgContainer">
                                    <ListGroup flush className="chat_msglist" id="chat_box">
                                        {this.state.chats.map((item, i) => (

                                            <ListGroupItem key={i}>
                                                {
                                                    i % 2 !== 0 && i !== 0 ? (
                                                        <div>
                                                            <b>Bot: </b> <i>{item}</i>
                                                        </div>
                                                    ) : <div>
                                                            {item}
                                                        </div>
                                                }
                                            </ListGroupItem>)
                                        )}
                                    </ListGroup>
                                </div>
                            </CardBody>
                            <CardFooter>
                                <Form onSubmit={this.sendMsg}>
                                    <FormGroup>
                                        <Row>
                                            <Col md="12">
                                                <Input onChange={this.handleInput} type="text" name="msg" id="exampleEmail" placeholder="Type something..." value={this.state.msg} requiered={this.state.msg.toString()} />
                                            </Col>
                                            {/* <Button md="2" color="success" type="submit" disabled={this.state.disabledLoginBtn}>
                                                <i className="nc-icon nc-send"></i>
                                            </Button> */}
                                        </Row>
                                    </FormGroup>
                                </Form>
                            </CardFooter>
                        </Card>
                    </Col>
                </div>
            </div>
        )
    }
}

const mapStateToProps = state => {
    counterpart.setLocale(state.language);
    return { lng: state.language }
}

const mapDispatchToProps = dispatch => ({});

export default connect(mapStateToProps, mapDispatchToProps)(ChatBot);