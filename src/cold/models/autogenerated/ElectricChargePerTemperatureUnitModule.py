
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class ElectricChargePerTemperatureUnit(SIDimensionalUnit):
    """
    Class representing the `ElectricChargePerTemperatureUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_200c735e_3dd7_44b2_bb34_4bb454a8e53b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricChargePerTemperatureUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricChargePerTemperatureUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_200c735e_3dd7_44b2_bb34_4bb454a8e53b',
    
    class_name='ElectricChargePerTemperatureUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_200c735e_3dd7_44b2_bb34_4bb454a8e53b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricChargePerTemperatureUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    