
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class EnergyLengthPerAmountUnit(SIDimensionalUnit):
    """
    Class representing the `EnergyLengthPerAmountUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8fb052e8_fcca_43ce_85db_55266baf2d7c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EnergyLengthPerAmountUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EnergyLengthPerAmountUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_8fb052e8_fcca_43ce_85db_55266baf2d7c',
    
    class_name='EnergyLengthPerAmountUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8fb052e8_fcca_43ce_85db_55266baf2d7c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EnergyLengthPerAmountUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    