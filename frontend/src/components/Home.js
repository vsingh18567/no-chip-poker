import React from 'react'

class Home extends React.Component {
    constructor(props) {
        super(props);
        this.user = props.user;
        this.isLoggedIn = this.user !== "";
        this.background_color = "#121212";
    }

    getNavBarText = function() {
        if (this.isLoggedIn) {
            return ["Profile", "Logout"];
        } else {
            return ["Login", "Register"];
        }
    }

    render() {
        return (
            <div id="header">
                <nav className="navbar">
                    <div className="container">
                        <div id="navMenu" className="navbar-menu">
                            <div className="navbar-start">
                                <a className="navbar-item">
                                    Home
                                </a>
                                <a className="navbar-item">
                                    About
                                </a>
                            </div>

                            <div className="navbar-end">
                                <div className="navbar-item">
                                    <div className="buttons">
                                        <a className="button is-dark">{this.getNavBarText()[0]}</a>
                                        <a className="button is-link">{this.getNavBarText()[1]}</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </nav>
                <section className="hero is-link is-fullheight-with-navbar">
                    <div className="hero-body has-text-centered">
                        <div className="container">
                            <p className="title" style={{fontSize: "4vw"}}>No Chip Poker</p>
                            <p className="subtitle">Have a deck of cards, but no chips? This is the website for you!</p>
                            <div className="box has-text-centered">
                                <button className="button is-one-fifth">Learn More</button>
                                <button className="button is-one-fifth">Get Started</button>

                            </div>
                        </div>
                    </div>
                </section>
            </div>

        );
    }
}

export default Home;