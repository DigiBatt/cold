
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NumberOfEntitiesModule import NumberOfEntities



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class NumberOfCellsConnectedInSeries(NumberOfEntities, ElectrochemicalQuantity):
    """
    Class representing the `NumberOfCellsConnectedInSeries` entity, which inherits from:
    - NumberOfEntities, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9d6a52ed_a53d_4327_a391_f173677a4b1d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NumberOfCellsConnectedInSeries'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NumberOfCellsConnectedInSeries(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9d6a52ed_a53d_4327_a391_f173677a4b1d',
    
    class_name='NumberOfCellsConnectedInSeries',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9d6a52ed_a53d_4327_a391_f173677a4b1d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NumberOfCellsConnectedInSeries',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    