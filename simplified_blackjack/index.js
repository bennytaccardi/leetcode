function play(hand) {
  console.log(hand);
  if (hand > 21) return 1;
  if (hand >= 17 && hand <= 21) return 0;
  if (hand === 16) return 0.5;
  const currentProb = hand > 11 ? 10 + hand - 21 : 0;
  console.log(currentProb);
  return (1 / 10) * play(hand + 1) + currentProb / 10;
}

console.log(play(13));
const cards = new Array(52).fill().map((e, i) => {
  return i + 1;
});

console.log(cards.sort(() => 0.5 - Math.random()));
