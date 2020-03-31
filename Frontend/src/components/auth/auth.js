class Auth{
    constructor(){
        this.authenticated = localStorage.getItem('token') || null;
    }

    login(cb, type){
        localStorage.setItem('token', JSON.stringify({dat: 'XXXX', userType: type}));
        this.authenticated = localStorage.getItem('token');
        // Retorna la ruta correspondiente al tipo de usuario
        cb(type);
    }

    logout(cb){
        // Debo cambiar ambos
        this.authenticated = null;
        localStorage.clear();
        cb();
    }

    isAuthenticated(){
        return this.authenticated !== null;
    }

    getType(){
        var t = JSON.parse(this.authenticated); 
        return t.userType;
    }
}

export default new Auth();