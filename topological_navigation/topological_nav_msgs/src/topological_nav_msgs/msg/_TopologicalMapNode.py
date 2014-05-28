"""autogenerated by genpy from topological_nav_msgs/TopologicalMapNode.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class TopologicalMapNode(genpy.Message):
  _md5sum = "4196506e57100b9489aeb84217464d1a"
  _type = "topological_nav_msgs/TopologicalMapNode"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Info stored with a node in a 2d topological map

# Id of this node in the topological map
uint32 id

# Dimensions of local grid.  The local grid covers the rectangle between
# (0,0) and (x_size, y_size) in the grid's frame
float32 x_size
float32 y_size

# Resolution of the local occupancy grid
float32 resolution


"""
  __slots__ = ['id','x_size','y_size','resolution']
  _slot_types = ['uint32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,x_size,y_size,resolution

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TopologicalMapNode, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.x_size is None:
        self.x_size = 0.
      if self.y_size is None:
        self.y_size = 0.
      if self.resolution is None:
        self.resolution = 0.
    else:
      self.id = 0
      self.x_size = 0.
      self.y_size = 0.
      self.resolution = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_I3f.pack(_x.id, _x.x_size, _x.y_size, _x.resolution))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.id, _x.x_size, _x.y_size, _x.resolution,) = _struct_I3f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_I3f.pack(_x.id, _x.x_size, _x.y_size, _x.resolution))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.id, _x.x_size, _x.y_size, _x.resolution,) = _struct_I3f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_I3f = struct.Struct("<I3f")