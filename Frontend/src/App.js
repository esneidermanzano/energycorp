import React from "react";
import { createBrowserHistory } from "history";
import { Router, Route, Switch, Redirect } from "react-router-dom";

import DashLayout from "layouts/DashLayout.jsx";
import Start from "views/Start.jsx";
import Login from "components/login/Login.jsx";
import GetBill from "components/GetBill.jsx";

import routesAdmin from "routes/adminRoutes.js";
import routesOperator from "routes/operatorRoutes.js";
import routesManager from "routes/managerRoutes.js";

import { ProtectedRoute, ProtectedLoginRoute } from "components/auth/ProtectedRoute.js";

const hist = createBrowserHistory();

function App() {
    return (
        <Router history={hist}>
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css" integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ==" crossOrigin="" />
            <script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js" integrity="sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew==" crossOrigin=""></script>

            <Switch>
                <Route exact path="/" component={Start} />
                <ProtectedLoginRoute exact path="/login" component={Login} />
                <Route exact path="/getBill" component={GetBill} />

                <ProtectedRoute path="/admin" userType="admin" render={props => <DashLayout {...props} routes={routesAdmin} loggedInBtn={true} />} />
                <ProtectedRoute path="/operator" userType="operator" render={props => <DashLayout {...props} routes={routesOperator} loggedInBtn={true} />} />
                <ProtectedRoute path="/manager" userType="manager" render={props => <DashLayout {...props} routes={routesManager} loggedInBtn={true} />} />

                <Redirect exact to="/" />
            </Switch>
        </Router>
    )
}

export default App;