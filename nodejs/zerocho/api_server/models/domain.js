const Sequelize = require("sequelize");

class Domain extends Sequelize.Model {
    static initiate(sequelize) {
        Domain.init({
            host: {
                type: Sequelize.STRING(60),
                allowNull: false,
            },
            type: {
                type: Sequelize.ENUM("free", "premium"),
                allowNull: false,
            }, // 무료/유료 고객 구분 결제 붙일 때 유용
            clientSecret: {
                type: Sequelize.UUID, // 고유 문자열 , 사용자마다 다른 값을 줄 떄 사용
                allowNull: false,
            }
        }, {
            sequelize,
            timestapms: true,
            paranoid: true,
            modelName: "Domain",
            tableName: "donamins",
        })
    }



}

module.exports = Domain;
