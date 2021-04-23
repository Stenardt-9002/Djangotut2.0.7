
import React ,{Component} from 'react' ;
import ReactDom from 'react-dom' ;

class App extends Component{
    render(){
        return <h1>Test React App</h1>
    }
}


ReactDOM.render(<App/> ,document.getElementById('app'));


