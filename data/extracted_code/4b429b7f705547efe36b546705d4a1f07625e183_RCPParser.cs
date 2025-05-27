
    public class RCPAddress {
        // parameters: X, Y, min, max, default, unit, type, UI?, r/w, scale
        // get: X, Y
        // set: X, Y, value, textValue


        public static string ToString (object instance) {
            Type currentType = instance.GetType();
            string result = string.Empty;

            while (currentType != null && currentType != typeof(object)) {
                if (currentType.DeclaringType == typeof(Console)) {
                    result = $"{currentType.Name}:{result}";
                    currentType = null;
                } else {
                    result = $"{currentType.Name}/{result}";
                    currentType = currentType.DeclaringType;
                }
            }

            return result.TrimEnd('/') + " " + instance;
        }

        public class Console {
            public class MIXER {

            }

            public class CL {

            }

            public class QL {

                public class Current {

                    public class CustomFaderBank {

                        public class SourceCh {
                            // 4 32 0 11 "NO ASSIGN" "" string any rw 1
                        }
                        public class Master {
                            public class SourceCh {
                                // 4 2 0 11 "NO ASSIGN" "" string any rw 1
                            }
                        }
                    }
                    public class FaderBank {
                        public enum FaderBanks {
                            I,
                            Dont,
                            Know
                        }
                        public class Select {
                            // 1 1 0 1 0 "" integer any rw 1
                            // TODO: what does it do?
                            public enum Selects {
                                BankA,
                                BankB
                            }
                            private readonly Selects? bank = null;
                            public Select () { }
                            public Select (Selects bank) { this.bank = bank; }
                            public override string ToString () {
                                return "0 0" + bank != null ? " " + bank.Value.ToString() : string.Empty;
                            }
                        }
                        public class Bank {
                            public enum Banks {
                                Input1,
                                Input2,
                                StInDCA,
                                MixMatrix,
                                B1,
                                B2,
                                B3,
                                B4
                            }
                            public class Recall {
                                // 1 3 0 8 0 "" integer any rw 1
                                // TODO: 3 banks, each with 8 options
                                public FaderBanks? faderBank = null;
                                public Banks? bank = null;
                                public Recall (FaderBanks faderBank) {
                                    this.faderBank = faderBank;
                                }
                                public Recall (FaderBanks faderBank, Banks bank) {
                                    this.faderBank = faderBank;
                                    this.bank = bank;
                                }
                                public override string ToString () {
                                    return "0 " + (int)faderBank.Value + (bank != null ? ' ' + ((int)bank.Value).ToString() : string.Empty);
                                }
                            }
                            public class Toggle {
                                // 1 1 0 8 0 "" integer any rw 1
                                // TODO: what does it do?
                            }
                        }
                    }
                }
            }
        }
    }