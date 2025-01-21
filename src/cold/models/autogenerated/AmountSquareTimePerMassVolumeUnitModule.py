
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class AmountSquareTimePerMassVolumeUnit(SIDimensionalUnit):
    """
    Class representing the `AmountSquareTimePerMassVolumeUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_052e9796_1144_43ae_a798_c5755cd6cd81'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AmountSquareTimePerMassVolumeUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AmountSquareTimePerMassVolumeUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_052e9796_1144_43ae_a798_c5755cd6cd81',
    
    class_name='AmountSquareTimePerMassVolumeUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_052e9796_1144_43ae_a798_c5755cd6cd81',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AmountSquareTimePerMassVolumeUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    