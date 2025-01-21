
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class EnergyPerAmountUnit(SIDimensionalUnit):
    """
    Class representing the `EnergyPerAmountUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0972cb08_48bd_4524_ac03_8a2e7f30f02f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EnergyPerAmountUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EnergyPerAmountUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_0972cb08_48bd_4524_ac03_8a2e7f30f02f',
    
    class_name='EnergyPerAmountUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0972cb08_48bd_4524_ac03_8a2e7f30f02f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EnergyPerAmountUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    