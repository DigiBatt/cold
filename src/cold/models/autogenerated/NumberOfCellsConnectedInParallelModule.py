
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NumberOfEntitiesModule import NumberOfEntities



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class NumberOfCellsConnectedInParallel(NumberOfEntities, ElectrochemicalQuantity):
    """
    Class representing the `NumberOfCellsConnectedInParallel` entity, which inherits from:
    - NumberOfEntities, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_482173dc_7779_4f12_982c_b19f2cda2dac'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NumberOfCellsConnectedInParallel'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NumberOfCellsConnectedInParallel(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_482173dc_7779_4f12_982c_b19f2cda2dac',
    
    class_name='NumberOfCellsConnectedInParallel',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_482173dc_7779_4f12_982c_b19f2cda2dac',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NumberOfCellsConnectedInParallel',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    