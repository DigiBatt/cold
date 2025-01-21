
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialModule import ElectricPotential



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class WorkingPotentialRange(ElectricPotential, ElectrochemicalQuantity):
    """
    Class representing the `WorkingPotentialRange` entity, which inherits from:
    - ElectricPotential, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c39b2498_783e_48e1_9814_6164bd99823c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'WorkingPotentialRange'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = WorkingPotentialRange(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c39b2498_783e_48e1_9814_6164bd99823c',
    
    class_name='WorkingPotentialRange',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c39b2498_783e_48e1_9814_6164bd99823c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'WorkingPotentialRange',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    