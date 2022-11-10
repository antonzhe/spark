#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spark/connect/commands.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyspark.sql.connect.proto import relations_pb2 as spark_dot_connect_dot_relations__pb2
from pyspark.sql.connect.proto import types_pb2 as spark_dot_connect_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1cspark/connect/commands.proto\x12\rspark.connect\x1a\x1dspark/connect/relations.proto\x1a\x19spark/connect/types.proto"\x94\x02\n\x07\x43ommand\x12N\n\x0f\x63reate_function\x18\x01 \x01(\x0b\x32#.spark.connect.CreateScalarFunctionH\x00R\x0e\x63reateFunction\x12H\n\x0fwrite_operation\x18\x02 \x01(\x0b\x32\x1d.spark.connect.WriteOperationH\x00R\x0ewriteOperation\x12_\n\x15\x63reate_dataframe_view\x18\x03 \x01(\x0b\x32).spark.connect.CreateDataFrameViewCommandH\x00R\x13\x63reateDataframeViewB\x0e\n\x0c\x63ommand_type"\x97\x04\n\x14\x43reateScalarFunction\x12\x14\n\x05parts\x18\x01 \x03(\tR\x05parts\x12P\n\x08language\x18\x02 \x01(\x0e\x32\x34.spark.connect.CreateScalarFunction.FunctionLanguageR\x08language\x12\x1c\n\ttemporary\x18\x03 \x01(\x08R\ttemporary\x12>\n\x0e\x61rgument_types\x18\x04 \x03(\x0b\x32\x17.spark.connect.DataTypeR\rargumentTypes\x12\x38\n\x0breturn_type\x18\x05 \x01(\x0b\x32\x17.spark.connect.DataTypeR\nreturnType\x12\x31\n\x13serialized_function\x18\x06 \x01(\x0cH\x00R\x12serializedFunction\x12\'\n\x0eliteral_string\x18\x07 \x01(\tH\x00R\rliteralString"\x8b\x01\n\x10\x46unctionLanguage\x12!\n\x1d\x46UNCTION_LANGUAGE_UNSPECIFIED\x10\x00\x12\x19\n\x15\x46UNCTION_LANGUAGE_SQL\x10\x01\x12\x1c\n\x18\x46UNCTION_LANGUAGE_PYTHON\x10\x02\x12\x1b\n\x17\x46UNCTION_LANGUAGE_SCALA\x10\x03\x42\x15\n\x13\x66unction_definition"\x96\x01\n\x1a\x43reateDataFrameViewCommand\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1b\n\tis_global\x18\x03 \x01(\x08R\x08isGlobal\x12\x18\n\x07replace\x18\x04 \x01(\x08R\x07replace"\xe6\x05\n\x0eWriteOperation\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x16\n\x06source\x18\x02 \x01(\tR\x06source\x12\x14\n\x04path\x18\x03 \x01(\tH\x00R\x04path\x12\x1f\n\ntable_name\x18\x04 \x01(\tH\x00R\ttableName\x12:\n\x04mode\x18\x05 \x01(\x0e\x32&.spark.connect.WriteOperation.SaveModeR\x04mode\x12*\n\x11sort_column_names\x18\x06 \x03(\tR\x0fsortColumnNames\x12\x31\n\x14partitioning_columns\x18\x07 \x03(\tR\x13partitioningColumns\x12\x43\n\tbucket_by\x18\x08 \x01(\x0b\x32&.spark.connect.WriteOperation.BucketByR\x08\x62ucketBy\x12\x44\n\x07options\x18\t \x03(\x0b\x32*.spark.connect.WriteOperation.OptionsEntryR\x07options\x1a:\n\x0cOptionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a[\n\x08\x42ucketBy\x12.\n\x13\x62ucket_column_names\x18\x01 \x03(\tR\x11\x62ucketColumnNames\x12\x1f\n\x0bnum_buckets\x18\x02 \x01(\x05R\nnumBuckets"\x89\x01\n\x08SaveMode\x12\x19\n\x15SAVE_MODE_UNSPECIFIED\x10\x00\x12\x14\n\x10SAVE_MODE_APPEND\x10\x01\x12\x17\n\x13SAVE_MODE_OVERWRITE\x10\x02\x12\x1d\n\x19SAVE_MODE_ERROR_IF_EXISTS\x10\x03\x12\x14\n\x10SAVE_MODE_IGNORE\x10\x04\x42\x0b\n\tsave_typeB"\n\x1eorg.apache.spark.connect.protoP\x01\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "spark.connect.commands_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\036org.apache.spark.connect.protoP\001"
    _WRITEOPERATION_OPTIONSENTRY._options = None
    _WRITEOPERATION_OPTIONSENTRY._serialized_options = b"8\001"
    _COMMAND._serialized_start = 106
    _COMMAND._serialized_end = 382
    _CREATESCALARFUNCTION._serialized_start = 385
    _CREATESCALARFUNCTION._serialized_end = 920
    _CREATESCALARFUNCTION_FUNCTIONLANGUAGE._serialized_start = 758
    _CREATESCALARFUNCTION_FUNCTIONLANGUAGE._serialized_end = 897
    _CREATEDATAFRAMEVIEWCOMMAND._serialized_start = 923
    _CREATEDATAFRAMEVIEWCOMMAND._serialized_end = 1073
    _WRITEOPERATION._serialized_start = 1076
    _WRITEOPERATION._serialized_end = 1818
    _WRITEOPERATION_OPTIONSENTRY._serialized_start = 1514
    _WRITEOPERATION_OPTIONSENTRY._serialized_end = 1572
    _WRITEOPERATION_BUCKETBY._serialized_start = 1574
    _WRITEOPERATION_BUCKETBY._serialized_end = 1665
    _WRITEOPERATION_SAVEMODE._serialized_start = 1668
    _WRITEOPERATION_SAVEMODE._serialized_end = 1805
# @@protoc_insertion_point(module_scope)
