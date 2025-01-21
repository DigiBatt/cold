
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class FrequencyPerVolumeUnit(SIDimensionalUnit):
    """
    Class representing the `FrequencyPerVolumeUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_43e499a1_ca67_4380_ac08_cfc52a93ad04'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FrequencyPerVolumeUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FrequencyPerVolumeUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_43e499a1_ca67_4380_ac08_cfc52a93ad04',
    
    class_name='FrequencyPerVolumeUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_43e499a1_ca67_4380_ac08_cfc52a93ad04',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FrequencyPerVolumeUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    