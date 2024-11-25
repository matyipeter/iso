from typing import List, Optional

from Signal import Signal


class Frame(object):
    id = 0  # type: int
    size = 0  # type: int
    signals = None  # type: List[Signal]
    multiplexer = None  # type: Optional[Signal]
    
    def __init__(
            self,
            frame_id: int,
            frame_size: int,
            frame_name: str = "",
    ) -> None:
        self.id = frame_id
        self.size = frame_size
        self.name = frame_name
        self.signals = []
    
    def _get_tuple(self):
        return (
            self.id,
            self.size
        )
    
    def add_signal(self, *args, **kwargs) -> bool:
        """Add a new signal directly to this frame. All arguments are passed on the the Signal constructor.
        
        :param args:
        :param kwargs:
        :return:        True if signal added. False otherwise.
        """
        signal = None
        
        if len(args) == 1 and isinstance(args[0], Signal):
            signal = args[0]
        else:
            try:
                signal = Signal(*args, **kwargs)
            except Exception as e:
                print(f"Failed to create signal: {str(e)}")
                return False
        
        self.signals.append(signal)
        
        if self.multiplexer is None and signal.is_multiplexer:
            self.multiplexer = signal
        elif signal.is_multiplexer:
            raise ValueError("Multiplexed signal added to frame, but frame already contains a root multiplexed signal.")
        
        return True
    
    def __str__(self) -> str:
        result = f"CAN Frame with name \"{self.name}\" and ID 0x{self.id:08X} - {self.size} bytes and {len(self.signals)} direct signals"
        
        for signal in self.signals:
            signal_str = str(signal)
    
            for line in signal_str.splitlines():
                result += f"\n\t{line}"
        
        if self.multiplexer:
            # TODO: Count multiplexed signals
            pass
        
        return result
    
    def __hash__(self) -> int:
        return hash(self._get_tuple())
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Frame):
            return NotImplemented
        
        return self._get_tuple() == other._get_tuple()
    
    pass