export const ATTENDANCE_STATUS_TEXT_COLOR: Record<ATTENDANCE_STATUS, string> = {
  [ATTENDANCE_STATUS.출석대기]: 'text-gray-300',
  [ATTENDANCE_STATUS.출석]: 'text-green-300',
  [ATTENDANCE_STATUS.지각]: 'text-yellow-300',
  [ATTENDANCE_STATUS.결석]: 'text-red-300',
};
