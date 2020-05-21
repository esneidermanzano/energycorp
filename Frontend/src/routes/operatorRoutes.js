import CreateClient from "views/operator/CreateClient.jsx";
import GetClients from "views/operator/GetClients.jsx";
import Payments from "views/operator/Payment.jsx";

var operatorRoutes = [
  {
    path: "/createClient",
    name: "createClient",
    icon: "nc-icon nc-diamond",
    component: CreateClient,
    layout: "/operator"
  },
  {
    path: "/getClients",
    name: "getClients",
    icon: "nc-icon nc-pin-3",
    component: GetClients,
    layout: "/operator"
  },
  {
    path: "/payments",
    name: "payments",
    icon: "nc-icon nc-credit-card",
    component: Payments,
    layout: "/operator"
  }
];

export default operatorRoutes;
