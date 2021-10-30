function solve() {
    class Balloon {
      constructor(color, gasWeight) {
        this.color = color
        this.gasWeight = gasWeight
      }
    }
  
    class PartyBalloon extends Balloon {
      constructor(color, gasWeight, ribbonColor, ribbonLenght) {
        super(color, gasWeight)
  
        this.ribbon = {color: ribbonColor, length: ribbonLenght}
      }
  
      get ribbon() {
        return this._ribbon
      }
    }
  
    class BirthdayBalloon extends PartyBalloon {
      constructor(color, gasWeight, ribbonColor, ribbonLenght, text) {
        super(color, gasWeight, ribbonColor, ribbonLenght)
  
        this.text = text
      }
  
      get text() {
        return this._text
      }
    }
  
    return {
      Balloon,
      PartyBalloon,
      BirthdayBalloon,
    }
  }
