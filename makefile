NAME = $(shell cat ./ipk/control/control | grep Package | cut -d" " -f2)
ARCH = $(shell cat ./ipk/control/control | grep Architecture | cut -d" " -f2)
VERSION = $(shell cat ./ipk/control/control | grep Version | cut -d" " -f2)
IPK_NAME = "${NAME}_${VERSION}_${ARCH}.ipk"
IPK_TMP = "tmp_ipk"

SERVICE_SRC = "./src"
SERVICE_DEST = "opt/victronenergy/${NAME}"

SERVICE_TEMPLATE_SRC = "./service-templates"
SERVICE_TEMPLATE_DEST = "opt/victronenergy/service-templates/${NAME}"

all:
	#echo "clean"
	#rm -rf ${IPK_TMP}

	mkdir -p ${IPK_TMP}
	echo "2.0" > ${IPK_TMP}/debian-binary

	echo "copying template files"
	cp -r ipk/data ${IPK_TMP}/
	cp -r ipk/control ${IPK_TMP}/

	echo "copying source files"
	mkdir -p ${IPK_TMP}/data/${SERVICE_DEST}/ && cp -r ${SERVICE_SRC}/* ${IPK_TMP}/data/${SERVICE_DEST}/
	mkdir -p ${IPK_TMP}/data/${SERVICE_TEMPLATE_DEST}/ &&  cp -r ${SERVICE_TEMPLATE_SRC}/* ${IPK_TMP}/data/${SERVICE_TEMPLATE_DEST}/

	echo "creating ipk..."
	cd ${IPK_TMP}/control && tar czvf ../control.tar.gz .
	cd ${IPK_TMP}/data && tar czvf ../data.tar.gz .
	cd ${IPK_TMP}/ && tar czvf "./${IPK_NAME}" ./control.tar.gz ./data.tar.gz ./debian-binary
	mv ${IPK_TMP}/${IPK_NAME} ./ipk/

	echo "clean"
	rm -rf ${IPK_TMP}

clean:
	rm -rf ${IPK_TEMP}
