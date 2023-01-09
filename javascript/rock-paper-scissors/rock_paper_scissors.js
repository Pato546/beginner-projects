const GUESS_OPTIONS = ["rock", "paper", "scissors"];

const getComputerChoice = () => {
  randomGuess = Math.trunc(Math.random() * 3);
  return GUESS_OPTIONS[randomGuess];
};

const playRound = (playerSelection, computerSelection) => {
  if (playerSelection === computerSelection) {
    return "Tie";
  }

  let msg = "rock beats scissors";
  if (playerSelection === "rock" && computerSelection === "scissors") {
    return `You Won! ${msg}`;
  } else if (playerSelection === "scissors" && computerSelection === "rock") {
    return `You Lose! ${msg}`;
  }

  msg = "paper beats rock";
  if (playerSelection === "paper" && computerSelection === "rock") {
    return `You Won! ${msg}`;
  } else if (playerSelection === "rock" && computerSelection === "paper") {
    return `You Lose! ${msg}`;
  }

  msg = "scissors beats paper";

  if (playerSelection === "scissors" && computerSelection === "paper") {
    return `You Won! ${msg}`;
  } else if (playerSelection === "paper" && computerSelection === "scissors") {
    return `You Lose! ${msg}`;
  }
};

const game = () => {
  playerScore = 0;
  computerScore = 0;

  for (let i = 0; i < 5; i++) {
    const playerSelection = prompt("enter guess: ");
    const computerSelection = getComputerChoice();

    let roundResult = playRound(playerSelection, computerSelection);

    if (roundResult.includes("You Won")) {
      ++playerScore;
    } else {
      ++computerScore;
    }
  }

  let gameOutcome =
    playerScore > computerScore
      ? `You won with ${playerScore} points`
      : `Computer won with ${computerScore} points`;

  return gameOutcome;
};

console.log(game());
