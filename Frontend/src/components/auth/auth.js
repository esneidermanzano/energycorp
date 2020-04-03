class Auth{
    constructor(){
        this.authenticated = localStorage.getItem('session') || null;
    }

    login(obj, cb){
        localStorage.setItem('session', JSON.stringify(obj));
        this.authenticated = localStorage.getItem('session');
        // Retorna la ruta correspondiente al tipo de usuario
        cb(obj.user_type_name);
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
        return t.user_type_name;
    }

    getSession(){
        return JSON.parse(this.authenticated); 
    }
}

export default new Auth();