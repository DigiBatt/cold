
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricConductanceModule import ElectricConductance



from .ElectrochemicalTransportQuantityModule import ElectrochemicalTransportQuantity







class InternalConductance(ElectricConductance, ElectrochemicalTransportQuantity):
    """
    Class representing the `InternalConductance` entity, which inherits from:
    - ElectricConductance, ElectrochemicalTransportQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0c9655c6_6b0b_4819_a219_f286ad196fa9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InternalConductance'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InternalConductance(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0c9655c6_6b0b_4819_a219_f286ad196fa9',
    
    class_name='InternalConductance',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0c9655c6_6b0b_4819_a219_f286ad196fa9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InternalConductance',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    