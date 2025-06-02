interface MockSignal {
  (): any; // Callable signature
  set: jasmine.Spy<(val: any) => void>;
  update: jasmine.Spy<() => void>;
  mutate: jasmine.Spy<() => void>;
}
