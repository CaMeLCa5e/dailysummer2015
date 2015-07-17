
class AvroGenericConverter extends Converter[AvroKey[GenericRecord], java.util.Map[String, Any]] {
	override def convert(obj: AvroKey[GenericRecord]): java.util.Map[String, Any] = {}

	def unpackRecord(record: GenericRecord): java.util.Map[String,Any] = {
		mapAsJavaMap(record.getSchema.getFields.map( f => (f.name, unpack(record.get(f.name), f.schema))).toMap)
	}
