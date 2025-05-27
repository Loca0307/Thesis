export type TimerConfig = {
  workMinutes: number;
  breakMinutes: number;
  numberOfRounds: number;
  autoStartBreak: boolean;
  autoStartWork: boolean;
};

export type TimerSound = {
  name: string;
  file: string;
  label: string;
};