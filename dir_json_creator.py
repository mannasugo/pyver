import os


class JsonRoutine(object):

  def __init__(self):
    self.globalScope = []
    self.globalJson = ''
    self.dirString = ''

  def listify(self, dir):
    localScope = []
    for subs in os.listdir(dir):
      localMap = {}
      localMap['title'] = subs
      localDir = dir + '\\' + subs + '\\'
      if os.path.isdir(localDir):
        localMap['subMap'] = []
        localMap['subMap'] = self.listify(localDir)
      localScope.append(localMap)
    return localScope

  def jsonify(self, dir):
    self.globalJson += '['
    for locals in os.listdir(dir):
      self.globalJson += '{"id": "' + locals + '"'
      localDir = dir + '\\' + locals + '\\'
      if os.path.isdir(localDir):
        self.globalJson += ', "childMap": '
        self.jsonify(localDir)
      self.globalJson += '}'
      if os.listdir(dir).index(locals) < len(os.listdir(dir)) - 1:
        self.globalJson += ','
    self.globalJson += ']'
    return self.globalJson

# Routine = JsonRoutine()
# print Routine.jsonify('C:\\tv')
