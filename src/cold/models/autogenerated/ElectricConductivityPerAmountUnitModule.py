
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class ElectricConductivityPerAmountUnit(SIDimensionalUnit):
    """
    Class representing the `ElectricConductivityPerAmountUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_89113866_31a4_4d19_bc83_7f7c1661ab73'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricConductivityPerAmountUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricConductivityPerAmountUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_89113866_31a4_4d19_bc83_7f7c1661ab73',
    
    class_name='ElectricConductivityPerAmountUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_89113866_31a4_4d19_bc83_7f7c1661ab73',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricConductivityPerAmountUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    