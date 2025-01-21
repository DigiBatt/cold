
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricCurrentModule import ElectricCurrent



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class DoubleLayerCurrent(ElectricCurrent, ElectrochemicalQuantity):
    """
    Class representing the `DoubleLayerCurrent` entity, which inherits from:
    - ElectricCurrent, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a56fc557_9dea_42e6_b936_e9d62dcaf84f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DoubleLayerCurrent'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DoubleLayerCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a56fc557_9dea_42e6_b936_e9d62dcaf84f',
    
    class_name='DoubleLayerCurrent',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a56fc557_9dea_42e6_b936_e9d62dcaf84f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DoubleLayerCurrent',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    