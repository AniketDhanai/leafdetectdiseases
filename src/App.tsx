import './App.css'
import Solution from './components/landing-page/about/solution'
import Hero from './components/landing-page/hero'
import Navbar from './components/navbar'

function App() {
  return (
    <div className='App'>
        <Navbar />
        <Hero />
        <Solution />
    </div>
  )
}

export default App
